
using ADCO.Pages;

namespace ADCO;

public partial class App : Application
{
	public App()
	{
		InitializeComponent();

		//MainPage = new AppShell();
		MainPage = new login_page();
	}
}
