using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ControllerScript : MonoBehaviour
{
    public GameObject spaceship;
    public Material mat;
    [Range(0, 1)] public float speed = 0.2f;

    GameObject startPosition;
    GameObject midPosition;
    GameObject endPosition;

    float currentTime;
    float startTime;

    // Start is called before the first frame update
    void Start()
    {
        startPosition = Object.Instantiate(spaceship);
        startPosition.name = "Start Position";
        startPosition.GetComponentInChildren<MeshRenderer>().material = mat;
        startPosition.GetComponentInChildren<BoxCollider>().enabled = false;

        midPosition = Object.Instantiate(spaceship);
        midPosition.name = "End Position";
        midPosition.GetComponentInChildren<MeshRenderer>().material = mat;
        midPosition.transform.rotation = Random.rotation;
        midPosition.GetComponentInChildren<BoxCollider>().enabled = false;

        endPosition = Object.Instantiate(spaceship);
        endPosition.name = "End Position";
        endPosition.GetComponentInChildren<MeshRenderer>().material = mat;
        endPosition.GetComponentInChildren<BoxCollider>().enabled = false;
        endPosition.transform.rotation = Random.rotation;

        startTime = Time.time;
    }



    // Update is called once per frame
    void Update()
    {



        //spaceship.transform.rotation = Quaternion.Euler(Vector3.Lerp(startPosition.transform.rotation.eulerAngles, endPosition.transform.rotation.eulerAngles, deltatime * speed));

        if(midPosition == null | endPosition == null)
        {
            Debug.Log("No Positon right now");
        }
        else
        {
            float deltatime = Time.time - startTime;
            Quaternion Q1, Q2;

            Q1 = Quaternion.Slerp(startPosition.transform.rotation, midPosition.transform.rotation, deltatime * speed);

            Q2 = Quaternion.Slerp(midPosition.transform.rotation, endPosition.transform.rotation, deltatime * speed);

            spaceship.transform.rotation = Quaternion.Slerp(Q1, Q2, deltatime * speed);

            if (deltatime * speed > 1)
            {
                startTime = Time.time;
            }
        }



    }

    public void ResetMidAndEnd()
    {
        
        Destroy(endPosition);
        Destroy(midPosition);
        spaceship.transform.position = startPosition.transform.position;
        spaceship.transform.rotation = startPosition.transform.rotation;

        midPosition = Object.Instantiate(spaceship);
        midPosition.name = "End Position";
        midPosition.GetComponentInChildren<MeshRenderer>().material = mat;
        midPosition.transform.rotation = Random.rotation;
        midPosition.GetComponentInChildren<BoxCollider>().enabled = false;

        endPosition = Object.Instantiate(spaceship);
        endPosition.name = "End Position";
        endPosition.GetComponentInChildren<MeshRenderer>().material = mat;
        endPosition.GetComponentInChildren<BoxCollider>().enabled = false;
        endPosition.transform.rotation = Random.rotation;
        speed += .05f;
    }
}
