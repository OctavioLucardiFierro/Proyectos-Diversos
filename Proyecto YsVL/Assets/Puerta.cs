using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

public class Puerta : MonoBehaviour
{
    [SerializeField] private GameObject LlaveDeLaPuerta;
    [SerializeField] private float ParaDondeSeAbre;
    private bool bloqueada = false;
    private bool TieneLaLLave = false;
    private Inventario inv;


    private void OnCollisionEnter2D(Collision2D collision) {
        if (collision.gameObject.CompareTag("PJ")) {
            Inventario inv = collision.gameObject.GetComponent<Inventario>();
            if (inv != null) {
                TieneLaLLave = false;
                foreach (GameObject item in inv.inventario) {
                    if (item == LlaveDeLaPuerta) {
                        TieneLaLLave = true;
                        break; // No necesitamos seguir buscando si ya encontramos la llave
                    }
                }
                if (TieneLaLLave && bloqueada == false) {
                    transform.Rotate(new Vector3(0, 0, ParaDondeSeAbre));
                    bloqueada = !bloqueada;
                }
            }
        }
    }
}
