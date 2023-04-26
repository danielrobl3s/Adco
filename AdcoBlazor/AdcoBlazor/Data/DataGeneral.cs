namespace AdcoBlazor.Data;

public class Client
{
	public int Id { get; set; }
	public string Nombre { get; set; }

	public string MetodoPago { get; set; }
	public string Documentos { get; set; }
	public string Fecha { get; set; }
	public string Observaciones { get; set; }
	public int CreatedBy { get; set; }

}

public class ProyectosList
{
	public int Id { get; set; }
	public string Proyecto { get; set; }

	public string institucion_empresa { get; set; }
	public DateTime fecha_inicio { get; set; }
	public DateTime fecha_termino { get; set; }
	public string telefono { get; set; }

	public string direccion { get; set; }

	public string ubicacion { get; set; }

	public int created_by { get; set; }

}


public class MaterialsData
{

	public int id { get; set; }

	public int created_by { get; set; }

	public int cantidad { get; set; }

	public string concepto { get; set; }

	public DateTime fecha { get; set; }

	public string recurso { get; set; }



}

public class GastosData
{

	public int id { get; set; }

	public string Concepto { get; set; }

	public int Monto { get; set; }

	public string metodo_pago { get; set; }

	public int Cobrador { get; set; }

	public DateTime Date { get; set; }

	public int created_by { get; set; }

}


public class TrabajadoresData
{

	public int id { get; set; }
	public string nombre { get; set; }

	public string telefono { get; set; }
	public string correo { get; set; }
	public string direccion { get; set; }




}



public class RecursosData
{

	public int id { get; set; }

	public int created_by { get; set; }

	public string nombre { get; set; }

	public string precio { get; set; }
	public string tipo { get; set; }

}
