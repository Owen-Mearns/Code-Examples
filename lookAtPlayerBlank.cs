//Author: Owen Mearns
//Purpose: Make a simple turret that looks at player then shoots.

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class lookAtPlayer : MonoBehaviour
{


    public GameObject projectile;
    public Transform muzzlePoint;
    public GameObject projectileParent;
    
    public float projectileSpeed = 1000;
    public float projectileLifespan = 5;
   
    
    //Variable for our look at target
    public Transform playerTarget;
    // Update is called once per frame
    private float coolDown;


    void Update()
    {
        if (coolDown > 0)
        {
            coolDown -= Time.deltaTime;
        }
    }
    
    //When PLayer gets clsoe enough to the turret, look at them
    private void OnTriggerStay(Collider other)
    {
        if(other.gameObject.tag == "Player")
        {
            Vector3 diff = playerTarget.position - transform.position;
            transform.right = -diff;

            if (coolDown > 0) return; //if theres still time left on cool down, don't shoot

            //Shoot at player
            GameObject currProjectile = Instantiate(projectile, muzzlePoint.position, muzzlePoint.rotation);
            currProjectile.transform.SetParent(projectileParent.transform);
            currProjectile.GetComponent<Rigidbody>().AddForce(muzzlePoint.up * projectileSpeed);

            coolDown = 3f;
            Destroy(currProjectile, projectileLifespan);
        }
        
    }
}
