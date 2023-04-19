namespace AdcoBlazor.Data;

public class MaterialsData
{

    public int Id_gasto { get; set; }

    public string Concepto { get; set; }

    public int Monto { get; set; }

	public string MetodoPago { get; set; }

	public int Cobrador => 32 + (int)(Id_gasto * 2);

	public DateTime Date { get; set; }


}
