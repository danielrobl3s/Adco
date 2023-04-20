using AdcoBlazor;

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

    private void accessButton_Clicked(object sender, EventArgs e)
    {
        Navigation.PushModalAsync(new login_page());

    }

    private void createButton_Clicked(object sender, EventArgs e)
    {
        Navigation.PushModalAsync(new MainPage());
 
    }
}