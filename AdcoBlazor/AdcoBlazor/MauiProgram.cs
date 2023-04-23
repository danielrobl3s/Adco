using Microsoft.Extensions.Logging;
using AdcoBlazor.Data;
using AdcoBlazor.Models;

using System.Net.Http;

using Microsoft.Extensions.DependencyInjection;
using Microsoft.Maui;
using Microsoft.Maui.Hosting;
using Microsoft.Maui.Controls.Hosting;
using Microsoft.Maui.Controls.Compatibility;
using Blazor.Extensions.Storage;
using Blazor.Extensions.Storage.Interfaces;

namespace AdcoBlazor;

public static class MauiProgram
{
	public static MauiApp CreateMauiApp()
	{
		var builder = MauiApp.CreateBuilder();
		builder
			.UseMauiApp<App>()
			.ConfigureFonts(fonts =>
			{
				fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
			});

		builder.Services.AddMauiBlazorWebView();
        // Registra el servicio HttpClient
        builder.Services.AddTransient<HttpClient>();


#if DEBUG
        builder.Services.AddBlazorWebViewDeveloperTools();
		builder.Logging.AddDebug();
#endif

		builder.Services.AddSingleton<WeatherForecastService>();
        builder.Services.AddSingleton<AuthenticationService>();
        builder.Services.AddSingleton<AppState>();




		builder.Services.AddSingleton<MaterialsDataService>();

		return builder.Build();


	}


}
