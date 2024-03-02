using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Inventario : MonoBehaviour
{
    public List<GameObject> inventario;
    [SerializeField] private Vector2 puntoSeleccionado;

    void AgregarAlInventario(GameObject item){
        inventario.Add(item);
    }

    private void OnTriggerEnter2D(Collider2D other) {
        if(other.CompareTag("Item")){
            GameObject objeto = other.gameObject;
            AgregarAlInventario(objeto);
            objeto.transform.position = puntoSeleccionado;
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
