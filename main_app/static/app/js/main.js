var app = angular.module("TODOSocial", ["ngRoute", "TODOSocialControllers"]);

app.config(["$routeProvider", function($routeProvider)
{
    $routeProvider.

    when("/",
    {
        templateUrl: "/static/app/partial_html/home.html", controller: "ListsController"
    }).
    when("/add_todo_list",
    {
        templateUrl: "/static/app/partial_html/add_todo_list.html", controller: "AddTODOListController"
    }).
    when("/add_task/:list_id",
    {
        templateUrl: "/static/app/partial_html/add_task.html", controller: "AddTaskController"
    }).
    when("/add_comment/:task_id",
    {
        templateUrl: "/static/app/partial_html/add_comment.html", controller: "AddCommentController"
    }).
    when("/edit_todo_list/:list_id",
    {
        templateUrl: "/static/app/partial_html/edit_todo_list.html", controller: "EditTODOListController"
    }).
    when("/edit_task/:task_id",
    {
        templateUrl: "/static/app/partial_html/edit_task.html", controller: "EditTaskController"
    }).
    otherwise(
    {
        redirectTo: "/"
    });
}]);