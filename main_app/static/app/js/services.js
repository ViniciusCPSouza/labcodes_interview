var appServices = angular.module("TODOSocialServices", []);

appServices.service("TODOList", function($http, $q, $location, Task)
{
    var self = this;

    this._set_tasks = function(task_url, todo_list, index)
    {
        return $q.all({task: Task.get(task_url),
                       todo_list: $q.when(todo_list),
                       task_index: $q.when(index)})
                .then(function(task_data)
                {
                    task_data.todo_list.tasks[task_data.task_index] = task_data.task;
                });
    }

    this.get = function(rest_url)
    {
        return $http.get(rest_url).then(function(todo_list_response)
        {
            var todo_list = todo_list_response.data;

            for (var j = 0; j < todo_list.tasks.length; j++)
            {
                self._set_tasks(todo_list.tasks[j], todo_list, j);
            }

            return $q.when(todo_list);
        });
    }

    this.all = function()
    {
        var todo_lists = [];
        var lists_url = "https://" + $location.host() + ":" + $location.port() + "/api/todo_lists/?format=json";

        return $http.get(lists_url).then(function(todo_lists_response)
        {
            var lists = todo_lists_response.data;

            for (var i = 0; i < lists.length; i++)
            {
                var todo_list = lists[i];

                todo_lists.push(todo_list);

                for (var j = 0; j < todo_list.tasks.length; j++)
                {
                    self._set_tasks(todo_list.tasks[j], todo_list, j);
                }
            }

        }).then(function()
        {
            return $q.when(todo_lists);
        });
    }

    this.del = function(obj_data)
    {
        return $http({
                        method : "DELETE",
                        url : "api/todo_lists/" + obj_data.id,
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                     });
    }

    this.add = function(obj_data)
    {
        return $http.post('api/todo_lists', obj_data,
                          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
    }

    this.update = function(obj_data)
    {
        return $http.post('api/todo_lists/' + obj_data.id, obj_data,
                          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}});
    }
});

appServices.service("Task", function($http, $q, Comment)
{
    this.get = function(rest_url)
    {
        return $http.get(rest_url).then(function(task_response)
        {
            var task = task_response.data;

            for (var j = 0; j < task.comments.length; j++)
            {
                $q.all({comment: Comment.get(task.comments[j]),
                        task: $q.when(task),
                        comment_index: $q.when(j)})
                .then(function(comment_data)
                {
                    comment_data.task.comments[comment_data.comment_index] = comment_data.comment;
                });
            }

            return $q.when(task);
        });
    }

    this.del = function(obj_data)
    {
        return $http({
                        method : "DELETE",
                        url : "api/tasks/" + obj_data.id,
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                     });
    }

    this.add = function(obj_data, list_id)
    {
        obj_data.parent_list = list_id;

        return $http.post('api/tasks', obj_data,
                          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
    }

    this.update = function(obj_data)
    {
        return $http.post('api/tasks/' + obj_data.id, obj_data,
                          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}});
    }
});

appServices.service("Comment", function($http, $q)
{
    this.get = function(rest_url)
    {
        return $http.get(rest_url).then(function(response)
        {
            var comment = response.data;

            $q.all({comment: $q.when(comment),
                   user: $http.get(comment.author)})
            .then(function(user_data)
            {
                user_data.comment.author = user_data.user.data.username;
            });

            return $q.when(comment);
        });
    }

    this.add = function(obj_data, task_id)
    {
        obj_data.parent_task = task_id;

        return $http.post('api/comments', obj_data,
                          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
    }
});
