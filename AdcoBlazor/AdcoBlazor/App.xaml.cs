namespace AdcoBlazor;
using ADCO.Pages;

using System.Net.Http;
using Microsoft.Extensions.DependencyInjection;
using Blazor.Extensions.Storage;
using Blazor.Extensions.Storage.Interfaces;

public partial class App : Application
{
	public App()
	{
		InitializeComponent();

        MainPage = new MainPage();
	}
}
