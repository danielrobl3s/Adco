using AdcoBlazor;

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

    private async void regButton_Clicked(object sender, EventArgs e)
    {
        Navigation.PushModalAsync(new reg_page());

    }

    private void accessButton_Clicked(object sender, EventArgs e)
    {
        Navigation.PushModalAsync(new MainPage());

    }
}