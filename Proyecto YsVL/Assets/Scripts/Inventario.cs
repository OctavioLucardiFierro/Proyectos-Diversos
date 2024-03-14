using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Inventario : MonoBehaviour
{
    public List<GameObject> inventario;
    [SerializeField] private Vector2 puntoSeleccionado;
    [SerializeField]private TextMeshProUGUI  textoInventario;
    private string textoActualInventario = "";
    private string nuevoTexto;

    void AgregarAlInventario(GameObject item){
        inventario.Add(item);
    }



    // Start is called before the first frame update
    void Start()
    {
        textoInventario = GameObject.FindGameObjectWithTag("Inventario").GetComponent<TextMeshProUGUI>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter2D(Collider2D other) {
        if(other.CompareTag("Item")){
            GameObject objeto = other.gameObject;
            nuevoTexto = objeto.name;
            textoActualInventario = textoInventario.text;
            textoInventario.text = textoActualInventario + nuevoTexto+"\n";
            AgregarAlInventario(objeto);
            objeto.transform.position = puntoSeleccionado;

        
        }
    }
}
