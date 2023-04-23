
using System.Net.Http.Headers;
using System.Net.Http.Json;
using AdcoBlazor.Data;

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
            var client = new HttpClient();
            var request = new HttpRequestMessage(HttpMethod.Get, "http://127.0.0.1:8000/module/clients/");
			request.Headers.Add("X-CSRFToken", "0c6t9fVh5ZwdcXtiEh1lfJdOZ04Xjd5g");
			request.Headers.Add("Authorization", "Bearer 48fb1be1912736a4012c97e9e442ecf7cc5b8a8e");
			request.Headers.Add("Cookie", "csrftoken=0c6t9fVh5ZwdcXtiEh1lfJdOZ04Xjd5g; sessionid=b8blvtggli9n2nl84ydshq1y01tvoz54");
			_httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
			var response = await client.SendAsync(request);
			response.EnsureSuccessStatusCode();
			Console.WriteLine(await response.Content.ReadAsStringAsync());

			if (response.IsSuccessStatusCode)
			{
				var clients = await response.Content.ReadFromJsonAsync<List<Client>>();
				return clients;
			}

			return new List<Client>(); // Devuelve una lista vacía en lugar de null
		}



	}

}
