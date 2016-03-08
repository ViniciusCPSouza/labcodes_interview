var appControllers = angular.module("TODOSocialControllers", ["TODOSocialServices"]);

appControllers.controller("ListsController", function($scope, TODOList)
{
    TODOList.all().then(function(todo_lists)
    {
        $scope.todo_lists = todo_lists;
    });
});

appControllers.controller("DeleteTODOListController", function($scope, $routeParams, TODOList)
{
    $scope.form_data = new Object();
    $scope.form_data.id = $routeParams.list_id;

    $scope.submitYes = function()
    {
        TODOList.del($scope.form_data).then(function(data) { window.history.back(); });
    }

    $scope.submitNo = function()
    {
        window.history.back();
    }
});

appControllers.controller("DeleteTaskController", function($scope, $routeParams, Task)
{
    $scope.form_data = new Object();
    $scope.form_data.id = $routeParams.task_id;

    $scope.submitYes = function()
    {
        Task.del($scope.form_data).then(function(data) { window.history.back(); });
    }

    $scope.submitNo = function()
    {
        window.history.back();
    }
});

appControllers.controller("AddCommentController", function($scope, $routeParams, $location, Comment)
{
    $scope.form_data = new Object();
    $scope.form_data.author = "https://" + $location.host() + ":" + $location.port() + "/api/users/" + current_user_id + "/?format=json";

    $scope.submit = function()
    {
        Comment.add($scope.form_data, $routeParams.task_id).then(function(data) { window.history.back(); });
    }
});

appControllers.controller("AddTODOListController", function($scope, TODOList)
{
    $scope.form_data = new Object();

    $scope.submit = function()
    {
        TODOList.add($scope.form_data).then(function(data) { window.history.back(); });
    }
});

appControllers.controller("AddTaskController", function($scope, $routeParams, Task)
{
    $scope.form_data = new Object();

    $scope.submit = function()
    {
        Task.add($scope.form_data, $routeParams.list_id).then(function(data) { window.history.back(); });
    }
});

appControllers.controller("EditTODOListController", function($scope, $http, $routeParams, $location, TODOList)
{
    $scope.form_data = new Object();
    $scope.form_data.id = $routeParams.list_id;

    var todo_list_url = "https://" + $location.host() + ":" + $location.port() + "/api/todo_lists/" + $routeParams.list_id + "/?format=json";

    TODOList.get(todo_list_url).then(function(todo_list)
    {
        $scope.form_data.title = todo_list.title;
    });

    $scope.submit = function()
    {
        TODOList.update($scope.form_data).then(function(data) { window.history.back(); });
    }
});

appControllers.controller("EditTaskController", function($scope, $http, $q, $routeParams, $location, Task)
{
    $scope.form_data = new Object();
    $scope.form_data.id = $routeParams.task_id;

    var task_url = "https://" + $location.host() + ":" + $location.port() + "/api/tasks/" + $routeParams.task_id + "/?format=json";

    Task.get(task_url).then(function(task)
    {
        $scope.form_data.description = task.description;
        $scope.form_data.deadline = task.deadline;
        $scope.form_data.done = task.done;
        $scope.task_id = task.pk;

        $scope.comments = task.comments;
    });

    $scope.submit = function()
    {
        Task.update($scope.form_data).then(function(data) { window.history.back(); });
    }
});

appControllers.controller("DummyController", function($scope){});