app.controller("ListsController", function($scope, $http, GetFromREST)
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
                GetFromREST.get(todo_list["tasks"][j]).then(function(task_data)
                {
                    todo_list_obj.tasks.push(task_data["description"]);
                });
            }
        }
    });
});