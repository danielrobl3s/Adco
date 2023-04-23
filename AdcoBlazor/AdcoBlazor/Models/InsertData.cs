using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace AdcoBlazor.Models
{
	public class InsertData
	{

		public async Task RegisterAsync(string nombre, string metodopago, string fecha, string documentos, string observaciones, string createdby)
		{
			using var httpClient = new HttpClient();
			var registerUrl = "http://127.0.0.1:8000/module/clients/";
			var registerData = new Dictionary<string, string>
	{
		{"nombre", nombre},
		{"metodo_pago", metodopago},
		{"fecha", fecha},
		{"documentos", documentos},
		{"observaciones", observaciones},

	};

			var content = new StringContent(JsonConvert.SerializeObject(registerData), Encoding.UTF8, "application/json");
			var response = await httpClient.PostAsync(registerUrl, content);

			if (response.IsSuccessStatusCode)
			{
				var responseContent = await response.Content.ReadAsStringAsync();
				Console.WriteLine($"Register response: {responseContent}"); // Imprimir la respuesta en la consola
			}
			else
			{
				Console.WriteLine($"Registration failed: {response.StatusCode}");
			}
		}
		public class Client
		{
			public string Nombre { get; set; }
			public string Apellido { get; set; }
			public string Ubicacion { get; set; }
			public decimal Monto { get; set; }
			public string MetodoPago { get; set; }
			public string Password { get; set; }
			public DateTime Fecha { get; set; }
			public string Documentos { get; set; }
			public string Observaciones { get; set; }
			public string CreatedBy { get; set; }
		}


	}

}
