var appServices = angular.module("TODOSocialServices", ["TODOConstants"]);

appServices.service("GetFromREST", function($http)
{
    this.get = function(url)
    {
        if (url.indexOf("https") <= -1 && url.indexOf("http") > -1)
        {
            url = url.replace("http", "https");
        }

        return $http.get(url).then(function(response)
        {
            return response.data;
        });
    }
});
