namespace AdcoBlazor.Data;

public class MaterialsDataService
{
    private static readonly string[] Observaciones = new[]
    {
        "si", "no", "la", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    };

    private static readonly string[] Concepto = new[]
    {
        "pago de materiales", "pago proveedores"
    };

    private static readonly string[] MetodoPago = new[]
{
        "Tarjeta", "Efectivo"
    };

    private static readonly string[] Documentos = new[]
    {
        "www.drive.com", "www.youtubr.com"
    };

    public Task<MaterialsData[]> GetMaterialsAsync(DateTime startDate)
    {
        return Task.FromResult(Enumerable.Range(1, 5).Select(index => new MaterialsData
		{
            Id_gasto  = Random.Shared.Next(1, 55),
            Concepto = Concepto[Random.Shared.Next(Concepto.Length)],
			Monto = Random.Shared.Next(2000, 10000),
			MetodoPago = MetodoPago[Random.Shared.Next(MetodoPago.Length)],
            Date = startDate.AddDays(index)

		}).ToArray());
    }
}

