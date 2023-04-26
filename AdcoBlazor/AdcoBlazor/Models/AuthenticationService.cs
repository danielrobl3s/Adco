
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text;
using AdcoBlazor.Data;
using AdcoBlazor.Models;

using Microsoft.AspNetCore.Components;
using Newtonsoft.Json;
using Microsoft.Extensions.DependencyInjection;

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
            var loginData = new Dictionary<string, string>
        {
            { "username", username },
            { "password", password }
        };

            var content = new StringContent(JsonConvert.SerializeObject(loginData), Encoding.UTF8, "application/json");


            var response = await _httpClient.PostAsJsonAsync("http://127.0.0.1:8000/api/login/", content);

            if (response.IsSuccessStatusCode)
            {
                var token = await response.Content.ReadAsStringAsync();
                return (true, token, username);
            }

            return (false, null, null);
        }

		IServiceProvider serviceProvider = new ServiceCollection().BuildServiceProvider();
		private readonly IServiceProvider _serviceProvider;



		public async Task<List<Client>> GetClientDataAsync(string token)
		{
			var appState = (AppState)_serviceProvider.GetService(typeof(AppState));


			var client = new HttpClient();
            var request = new HttpRequestMessage(HttpMethod.Get, "http://127.0.0.1:8000/module/clients/");
			request.Headers.Add("X-CSRFToken", appState.CSRFToken);
			request.Headers.Add("Authorization", $"Bearer {appState.Barear}");
			request.Headers.Add("Cookie", $"csrftoken={appState.CSRFToken}; sessionid={appState.SesionId}");
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

		public async Task<List<ProyectosList>> GetProyectosDataAsync(string token)
		{
			var appState = (AppState)_serviceProvider.GetService(typeof(AppState));

			var client = new HttpClient();
			var request = new HttpRequestMessage(HttpMethod.Get, "http://127.0.0.1:8000/proyectos/");
			request.Headers.Add("X-CSRFToken", appState.CSRFToken);
			request.Headers.Add("Authorization", $"Bearer {appState.Barear}");
			request.Headers.Add("Cookie", $"csrftoken={appState.CSRFToken}; sessionid={appState.SesionId}");
			var response = await client.SendAsync(request);
			response.EnsureSuccessStatusCode();
			Console.WriteLine(await response.Content.ReadAsStringAsync());

			if (response.IsSuccessStatusCode)
			{
				var proyectos = await response.Content.ReadFromJsonAsync<List<ProyectosList>>();
				return proyectos;
			}

			return new List<ProyectosList>(); // Devuelve una lista vacía en lugar de null
		}


	}

}
