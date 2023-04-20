namespace AdcoBlazor;
using ADCO.Pages;

public partial class App : Application
{
	public App()
	{
		InitializeComponent();

		MainPage = new login_page();
	}
}
