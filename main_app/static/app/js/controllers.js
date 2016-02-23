var appControllers = angular.module("TODOSocialControllers", ["TODOSocialServices"]);

appControllers.controller("ListsController", function($scope, $q, GetFromREST)
{
    GetFromREST.get("http://localhost:8000/api/todo_lists/?format=json").then(function(todo_data)
    {
        $scope.todo_lists = [];

        for(var i = 0; i < todo_data.length; i++)
        {
            var todo_list = todo_data[i];
            var todo_list_obj = new Object();

            todo_list_obj.title = todo_list["title"];
            todo_list_obj.tasks = [];

            $scope.todo_lists.push(todo_list_obj);

            for (var j = 0; j < todo_list["tasks"].length; j++)
            {
                $q.all({task_data: GetFromREST.get(todo_list["tasks"][j]),
                        todo_list: $q.when(todo_list_obj)})
                .then(function(data)
                {
                    data.todo_list.tasks.push(data.task_data["description"]);
                });
            }
        }
    });
});