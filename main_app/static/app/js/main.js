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
        templateUrl: "", controller: ""
    }).
    when("/add_task",
    {
        templateUrl: "", controller: ""
    }).
    when("add_comment",
    {
        templateUrl: "", controller: ""
    }).
    when("edit_task",
    {
        templateUrl: "", controller: ""
    }).
    when("delete_todo_list",
    {
        templateUrl: "", controller: ""
    }).
    when("delete_task",
    {
        templateUrl: "", controller: ""
    }).
    otherwise(
    {
        redirectTo: "/"
    });
}]);