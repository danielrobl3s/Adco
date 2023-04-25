//using AdcoBlazor.Subtables;
//using Newtonsoft.Json;
//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Net.Http.Headers;
//using System.Text;
//using System.Threading.Tasks;

//namespace AdcoBlazor.Models
//{
//	internal class Subclients
//	{
//		public Task<List<Subclients>> GetClientDataAsync(string token, string userId)
//		{
//			return GetClientDataAsync(token, userId, Id_clientes);
//		}

//		public async Task<List<Subclients>> GetClientDataAsync(string token, string userId, List<Subclients> clients)
//		{
//			using (var httpClient = new HttpClient())
//			{
//				httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

//				var response = await httpClient.GetAsync($"your_api_endpoint_here?id={userId}");
//				var jsonContent = await response.Content.ReadAsStringAsync();
//				var clients = JsonConvert.DeserializeObject<List<Subclients>>(jsonContent);

//				return clients;
//			}
//		}

//	}
//}
