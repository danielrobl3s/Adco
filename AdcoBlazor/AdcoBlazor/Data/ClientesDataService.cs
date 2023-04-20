namespace AdcoBlazor.Data;

public class ClientesDataService
{
    private static readonly string[] Observaciones = new[]
    {
        "si", "no", "la", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    };

    private static readonly string[] Nombre = new[]
    {
        "pedro", "paco", "siso", "s"
    };

    private static readonly string[] MetodoPago = new[]
{
        "Tarjeta", "Efectivo"
    };

    private static readonly string[] Documentos = new[]
    {
        "www.drive.com", "www.youtubr.com"
    };



    public Task<ClientesData[]> GetClientesAsync(DateTime startDate)
    {
        return Task.FromResult(Enumerable.Range(1, 5).Select(index => new ClientesData
        {
            ID = Random.Shared.Next(1, 55),
            Nombre = Nombre[Random.Shared.Next(Nombre.Length)],
            MetodoPago = MetodoPago[Random.Shared.Next(MetodoPago.Length)],
            Date = startDate.AddDays(index),
            Documentos = Documentos[Random.Shared.Next(Documentos.Length)],

            Observaciones = Observaciones[Random.Shared.Next(Observaciones.Length)],

        }).ToArray());
    }
}

