namespace AdcoBlazor.Data;

public class INavigationService
{
	internal HttpClient httpClient;

	public int ID { get; set; }

    public string Nombre { get; set; }

    public string MetodoPago { get; set; }

    public DateTime Date { get; set; }

    public string Documentos { get; set; }

    public string Observaciones { get; set; }

    public int AñadidoPor { get; set; }

}
