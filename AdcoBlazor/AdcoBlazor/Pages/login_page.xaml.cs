using AdcoBlazor;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using Newtonsoft.Json;


namespace ADCO.Pages;


public partial class login_page : ContentPage
{
	public login_page()
	{
		InitializeComponent();
	}

    private void OnShowPasswordClicked(object sender, EventArgs e)
    {
        if (pass.IsPassword)
        {
            pass.IsPassword = false;
            showPasswordButton.Source = "hide.png";
        }
        else
        {
            pass.IsPassword = true;
            showPasswordButton.Source = "show.png";
        }
    }

	public async Task LoginAsync(string username, string password)
	{
		using var httpClient = new HttpClient();
		var loginUrl = "http://127.0.0.1:8000/api/login/";
		var loginData = new Dictionary<string, string>
	{
		{"username", username},

		{"password", password}
	};

		var content = new StringContent(JsonConvert.SerializeObject(loginData), Encoding.UTF8, "application/json");
		var response = await httpClient.PostAsync(loginUrl, content);

		if (response.IsSuccessStatusCode)
		{
			var responseContent = await response.Content.ReadAsStringAsync();
			Navigation.PushModalAsync(new MainPage());
			Console.WriteLine($"Login response: {responseContent}"); // Imprimir la respuesta en la consola
		}
		else
		{
			Console.WriteLine($"Login failed: {response.StatusCode}");
		}
	}
	private async void accessButton_Clicked(object sender, EventArgs e)
	{
		var username = user.Text;
		var password = pass.Text;

		if (string.IsNullOrWhiteSpace(username) || string.IsNullOrWhiteSpace(password))
		{
			// Mostrar mensaje de error (por ejemplo, usando un cuadro de diálogo)
			return;
		}

		await LoginAsync(username, password);
	}



	private async void regButton_Clicked(object sender, EventArgs e)
    {
        Navigation.PushModalAsync(new reg_page());

    }

}