var appControllers = angular.module("TODOSocialControllers", ["TODOSocialServices"]);

appControllers.controller("ListsController", function($scope, $q, $location, GetFromREST)
{
    GetFromREST.get("https://" + $location.host() + ":" + $location.port() + "/api/todo_lists/?format=json").then(function(todo_data)
    {
        $scope.todo_lists = [];

        for(var i = 0; i < todo_data.length; i++)
        {
            var todo_list = todo_data[i];
            var todo_list_obj = new Object();

            todo_list_obj.title = todo_list["title"];
            todo_list_obj.id = todo_list["pk"]
            todo_list_obj.tasks = [];

            $scope.todo_lists.push(todo_list_obj);

            for (var j = 0; j < todo_list["tasks"].length; j++)
            {
                $q.all({task_data: GetFromREST.get(todo_list["tasks"][j]),
                        todo_list: $q.when(todo_list_obj)})
                .then(function(data)
                {
                    task_obj = new Object();

                    task_obj.desc = data.task_data["description"]
                    task_obj.id = data.task_data["pk"]

                    data.todo_list.tasks.push(task_obj);
                });
            }
        }
    });
});

appControllers.controller("DeleteTODOListController", function($scope, $http, $routeParams)
{
    $scope.form_data = new Object();

    $scope.submitYes = function()
    {
        $scope.form_data.id = $routeParams.list_id;

        $http.post('delete/todo_lists', $scope.form_data,
                   {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).success(function(data) { window.history.back(); });
    }

    $scope.submitNo = function()
    {
        window.history.back();
    }
});

appControllers.controller("DeleteTaskController", function($scope, $http, $routeParams)
{
    $scope.form_data = new Object();

    $scope.submitYes = function()
    {
        $scope.form_data.id = $routeParams.task_id;

        $http.post('delete/tasks', $scope.form_data,
                   {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).success(function(data) { window.history.back(); });
    }

    $scope.submitNo = function()
    {
        window.history.back();
    }
});

appControllers.controller("AddCommentController", function($scope, $http, $routeParams)
{
    $scope.form_data = new Object();
    $scope.form_data.parent_task = $routeParams.task_id

    $scope.submit = function()
    {
        $http.post('forms/comments', $scope.form_data,
                   {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).success(function(data) { window.history.back(); });
    }
});

appControllers.controller("AddTODOListController", function($scope, $http)
{
    $scope.form_data = new Object();

    $scope.submit = function()
    {
        $http.post('forms/todo_lists', $scope.form_data,
                   {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).success(function(data) { window.history.back(); });
    }
});

appControllers.controller("AddTaskController", function($scope, $http, $routeParams)
{
    $scope.form_data = new Object();
    $scope.form_data.parent_list = $routeParams.list_id

    $scope.submit = function()
    {
        $http.post('forms/tasks', $scope.form_data,
                   {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).success(function(data) { window.history.back(); });
    }
});

appControllers.controller("EditTODOListController", function($scope, $http, $routeParams, GetFromREST)
{
    $scope.form_data = new Object();
    $scope.form_data.id = $routeParams.list_id

    var url = "https://" + $location.host() + ":" + $location.port() + "/api/todo_lists/" + $routeParams.list_id + "/?format=json";

    GetFromREST.get(url).then(function(todo_data)
    {
        $scope.form_data.title = todo_data["title"];
    });

    $scope.submit = function()
    {
        $http.post('forms/todo_lists', $scope.form_data,
                   {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).success(function(data) { window.history.back(); });
    }
});

appControllers.controller("EditTaskController", function($scope, $http, $q, $routeParams, $location, GetFromREST)
{
    $scope.form_data = new Object();
    $scope.form_data.id = $routeParams.task_id

    var url = "https://" + $location.host() + ":" + $location.port() + "api/tasks/" + $routeParams.task_id + "/?format=json";

    GetFromREST.get(url).then(function(task_data)
    {
        $scope.form_data.description = task_data["description"];
        $scope.form_data.deadline = task_data["deadline"];
        $scope.form_data.done = task_data["done"];
        $scope.task_id = task_data["pk"];

        $scope.form_data.comments = [];

        for (var j = 0; j < task_data["comments"].length; j++)
        {
            $q.all({comment_data: GetFromREST.get(task_data["comments"][j]),
                    form_data: $q.when($scope.form_data)})
            .then(function(data)
            {
                comment_obj = new Object();

                comment_obj.text = data.comment_data["text"]

                data.form_data.comments.push(comment_obj);

                $q.all({user_data: GetFromREST.get(data.comment_data["author"]),
                        comment: $q.when(comment_obj)})
                .then(function(get_data)
                {
                    get_data.comment.author = get_data.user_data["username"]
                });
            });
        }
    });

    $scope.submit = function()
    {
        $http.post('forms/tasks', $scope.form_data,
                   {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).success(function(data) { window.history.back(); });
    }

    $scope.$watch(function(scope)
                  {
                    return scope.form_data.done;
                  },
                  function(new_value, old_value)
                  {
                    if (new_value)
                    {
                        if (new_value == true)
                        {
                            FB.ui({
                                    method: 'share',
                                    name: "I've completed task '" + $scope.form_data.description + "'!",
                                    link: $location.absUrl().split('?')[0],
                                    picture: 'https://orig07.deviantart.net/2045/f/2011/022/d/5/adventure_time_ocean_of_fear_by_xrq0000000_a-d37tnax.jpg',
                                    caption: "Weird shit.",
                                    description: 'Stuff Stuff Stuff',
                                    message: ''
                                  });
                        }
                    }
                  });
});

appControllers.controller("DummyController", function($scope){});