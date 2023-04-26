
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text;
using AdcoBlazor.Data;
using Newtonsoft.Json;

namespace AdcoBlazor.Models
{
	public class DeleteClientService
	{
		public async Task<bool> DeleteClient(int clientId, string csrfToken, string barear, string sessionId)
		{
			var client = new HttpClient();
			var request = new HttpRequestMessage(HttpMethod.Delete, $"http://127.0.0.1:8000/module/clients/{clientId}/");
			request.Headers.Add("X-CSRFToken", csrfToken);
			request.Headers.Add("Authorization", barear);
			request.Headers.Add("Cookie", sessionId);
			var response = await client.SendAsync(request);

			if (response.IsSuccessStatusCode)
			{
				return true;
			}
			else
			{
				Console.WriteLine($"Error deleting client with ID {clientId}: {response.ReasonPhrase}");
				return false;
			}
		}
	}

}
