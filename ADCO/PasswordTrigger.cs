using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ADCO
{
    internal class PasswordTrigger : TriggerAction<ImageButton>, INotifyPropertyChanged
    {
        public string ShowIcon { get; set; }
        public string HideIcon { get; set; }
        bool _hidePassword = true;
        public bool HidePassword
        {
            get => _hidePassword;
            set
            {
                if (_hidePassword != value)
                {
                    _hidePassword = value;
                    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nameof(HidePassword)));
                }
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected override void Invoke(ImageButton sender)
        {
            sender.Source = HidePassword ? ShowIcon : HideIcon;
            HidePassword = !HidePassword;
        }
    }
}
