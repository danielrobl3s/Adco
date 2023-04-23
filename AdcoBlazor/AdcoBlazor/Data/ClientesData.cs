namespace AdcoBlazor.Data;

public class Client
{
	public int Id { get; set; }
	public string Nombre { get; set; }

	public string MetodoPago { get; set; }
	public string Documentos { get; set; }
	public string Observaciones { get; set; }

	public int CreatedBy { get; set; }


}