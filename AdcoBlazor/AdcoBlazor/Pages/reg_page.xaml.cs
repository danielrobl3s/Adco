using AdcoBlazor;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using Newtonsoft.Json;

namespace ADCO.Pages;

public partial class reg_page : ContentPage
{
	public reg_page()
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

	public async Task RegisterAsync(string username, string email, string password)
	{
		using var httpClient = new HttpClient();
		var registerUrl = "http://127.0.0.1:8000/api/registration/";
		var registerData = new Dictionary<string, string>
	{
		{"username", username},
		{"email", email},
		{"password1", password},
		{"password2", password}
	};

		var content = new StringContent(JsonConvert.SerializeObject(registerData), Encoding.UTF8, "application/json");
		var response = await httpClient.PostAsync(registerUrl, content);

		if (response.IsSuccessStatusCode)
		{
			var responseContent = await response.Content.ReadAsStringAsync();
			Navigation.PushModalAsync(new MainPage());
			Console.WriteLine($"Register response: {responseContent}"); // Imprimir la respuesta en la consola
		}
		else
		{
			Console.WriteLine($"Registration failed: {response.StatusCode}");
		}
	}

	private async void createButton_Clicked(object sender, EventArgs e)
	{
		var username = user.Text;
		var email = correo.Text;
		var password = pass.Text;

		if (string.IsNullOrWhiteSpace(username) || string.IsNullOrWhiteSpace(email) || string.IsNullOrWhiteSpace(password))
		{
			// Mostrar mensaje de error (por ejemplo, usando un cuadro de diálogo)
			return;
		}

		await RegisterAsync(username, email, password);
	}



	private void accessButton_Clicked(object sender, EventArgs e)
    {
        Navigation.PushModalAsync(new login_page());

    }

}