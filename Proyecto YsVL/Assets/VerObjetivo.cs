using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class VerObjetivo : MonoBehaviour
{
    public Transform objectToFollow; // Referencia al objeto que la cámara seguirá
    public Camera secondaryCamera;
    public RawImage uiImage;
    public RenderTexture cameraTexture;

    void Update()
    {
        // Asegúrate de tener un objeto para seguir
        if (objectToFollow == null)
        {
            Debug.LogWarning("No se ha asignado un objeto para seguir en el script CameraUIController.");
            return;
        }

        // Actualizar la posición y la rotación de la cámara secundaria para que siga al objeto
        secondaryCamera.transform.position = objectToFollow.position;
        secondaryCamera.transform.rotation = objectToFollow.rotation;

        // Actualizar la textura con la vista de la cámara secundaria
        RenderTexture.active = cameraTexture;
        secondaryCamera.Render();
        RenderTexture.active = null;

        // Mostrar la textura en el UI
        uiImage.texture = cameraTexture;
    }
}
