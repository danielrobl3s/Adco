using ADCO.Pages;

namespace AdcoBlazor;

public partial class App : Application
{
	public App()
	{
		InitializeComponent();

		MainPage = new login_page();
	}
}
