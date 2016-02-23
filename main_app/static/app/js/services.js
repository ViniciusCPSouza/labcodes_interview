app.service("GetFromREST", function($http)
{
    this.get = function(url)
    {
        return $http.get(url).then(function(response)
        {
            return response.data;
        });
    }
});
