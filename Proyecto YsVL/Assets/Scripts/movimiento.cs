using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class movimiento : MonoBehaviour
{
    [SerializeField]private float velo = 2f;

    private Rigidbody2D jugador;
    private Vector2 movi;
    private Animator anim;

    void Start()
    {
        jugador = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        float movX = Input.GetAxisRaw("Horizontal");
        float movY = Input.GetAxisRaw("Vertical");
        movi = new Vector2(movX, movY).normalized;

        anim.SetFloat("Horizontal", movX);
        anim.SetFloat("Vertical", movY);
        anim.SetFloat("velocidad", movi.sqrMagnitude);
    }

    private void FixedUpdate()
    {
        jugador.MovePosition(jugador.position + movi * velo * Time.fixedDeltaTime);

    }


}
