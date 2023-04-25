
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text;
using AdcoBlazor.Data;
using Newtonsoft.Json;

namespace AdcoBlazor.Models
{
    public class DeleteModel
    {
        private readonly HttpClient _httpClient;

		/**	private async Task DeleteClient(int clientId)
			{
				var client = new HttpClient();
				var request = new HttpRequestMessage(HttpMethod.Delete, $"http://127.0.0.1:8000/module/clients/{clientId}/");

				request.Headers.Add("X-CSRFToken", "0c6t9fVh5ZwdcXtiEh1lfJdOZ04Xjd5g");
				request.Headers.Add("Authorization", "Bearer 48fb1be1912736a4012c97e9e442ecf7cc5b8a8e");
				request.Headers.Add("Cookie", "csrftoken=0c6t9fVh5ZwdcXtiEh1lfJdOZ04Xjd5g; sessionid=b8blvtggli9n2nl84ydshq1y01tvoz54");

				var response = await client.SendAsync(request);

				if (response.IsSuccessStatusCode)
				{
					Clients = Clients.Where(client => client.Id != clientId).ToList();
					StateHasChanged();
					Console.WriteLine("Success: " + await response.Content.ReadAsStringAsync());
				}
				else
				{
					Console.WriteLine("Error: " + await response.Content.ReadAsStringAsync());
				}
			}
			**/
	}

}
