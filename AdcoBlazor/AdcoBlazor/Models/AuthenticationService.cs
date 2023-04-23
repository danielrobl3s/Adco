
using System.Net.Http.Headers;
using System.Net.Http.Json;

namespace AdcoBlazor.Models
{
    public class AuthenticationService
    {
        private readonly HttpClient _httpClient;

        public AuthenticationService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<(bool success, string token, string username)> LoginAsync(string username, string password)
        {
            var loginModel = new
            {
                username = username,
                password = password
            };

            var response = await _httpClient.PostAsJsonAsync("http://127.0.0.1:8000/api/login/", loginModel);

            if (response.IsSuccessStatusCode)
            {
                var token = await response.Content.ReadAsStringAsync();
                return (true, token, username);
            }

            return (false, null, null);
        }

        public async Task<List<Client>> GetClientDataAsync(string token)
        {
            _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
            var response = await _httpClient.GetAsync("http://127.0.0.1:8000/module/clients/");

            if (response.IsSuccessStatusCode)
            {
                var clients = await response.Content.ReadFromJsonAsync<List<Client>>();
                return clients;
            }

            return null;
        }

        public class Client
        {
            public int Id { get; set; }
            public string Nombre { get; set; }

            public string MetodoPago { get; set; }
            public string Fecha { get; set; }
            public string Documentos { get; set; }
            public string Observaciones { get; set; }

            public int CreatedBy { get; set; }


        }
    }

}
