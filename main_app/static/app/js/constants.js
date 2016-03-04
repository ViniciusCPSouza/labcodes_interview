var constantsApp = angular.module("TODOConstants", []);

var getProtocol = function()
{
	var LOCALHOSTS = ["127.0.0.1", "localhost"];
	var result = "https://";

	if (LOCALHOSTS.indexOf(window.location.hostname) != -1)
	{
		result = "http://";
	}	

	return result;
}

var getBaseURL = function()
{
	return getProtocol() + window.location.hostname + ":" + window.location.port;
}

constantsApp.constant("CONFIG", Object.freeze(
{
	BASE_URL = getBaseURL(),
	REST_TODO_LISTS_URL = "/api/todo_lists",
	REST_TASKS_URL = "/api/tasks",
	REST_JSON_FORMAT_PARAM = "/?format=json"
}));