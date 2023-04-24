using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace AdcoBlazor.Models
{
	public class InsertData
	{
		public async Task<bool> RegisterAsync(Client NewClient, string token, string csrfToken, string cookie)
		{
			try
			{
				var client = new HttpClient();
				var request = new HttpRequestMessage(HttpMethod.Post, "http://127.0.0.1:8000/module/clients/");

				// Agrega los encabezados necesarios
				request.Headers.Add("X-CSRFToken", csrfToken);
				request.Headers.Add("Authorization", token); 
				request.Headers.Add("Cookie", cookie);

				// Agrega el JSON del objeto 'newClient' en el cuerpo del mensaje
				request.Content = new StringContent(JsonConvert.SerializeObject(NewClient), Encoding.UTF8, "application/json");

				var response = await client.SendAsync(request);

				if (response.IsSuccessStatusCode)
				{
					var responseContent = await response.Content.ReadAsStringAsync();
					Console.WriteLine($"Register response: {responseContent}"); // Imprimir la respuesta en la consola
					return true; // Indica que se ha completado con éxito
				}
			}
			catch (Exception ex)
			{
				Console.WriteLine(ex.ToString()); // Agregar esta línea para ver detalles de excepción
			}

			return false; // Indica que ha ocurrido un error
		}


		public class Client
		{
			public string Nombre { get; set; }
			public string MetodoPago { get; set; }
			public string Documentos { get; set; }
			public string Observaciones { get; set; }
			public string CreatedBy { get; set; }
		}
	}
}
