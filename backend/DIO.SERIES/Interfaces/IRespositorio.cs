using System.Collections.Generic;

namespace DIO.SERIES.interfaces{
 
 public interface IResposiorio<T>
 {
     List<T> List();
     T RetornaPorId(int id);
     void insere( T entidade);
     void Exclui(int id);
     void Atualiza(int id, T entidade);

     int ProximoId();
 }



}
