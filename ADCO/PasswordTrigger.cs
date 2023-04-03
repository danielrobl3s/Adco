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

        private bool isPasswordHidden = true;
        public bool IsPasswordHidden
        {
            get => isPasswordHidden;
            set
            {
                if (isPasswordHidden != value)
                {
                    isPasswordHidden = value;
                    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nameof(IsPasswordHidden)));
                }
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected override void Invoke(ImageButton sender)
        {
            sender.Source = IsPasswordHidden ? ShowIcon : HideIcon;
            isPasswordHidden = !IsPasswordHidden;
        }
    }
}
