//Author: Owen Mearns
//Purpose: Use Unity's built in nav mesh to make a simple enemy AI

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class NavMeshAI : MonoBehaviour
{
    public enum EnemyState
    {
        patrol,
        chase
    }
    public EnemyState currentState = EnemyState.patrol;

    public Transform[] wayPoints;
    public int currentWayPointIdx = 0;
    public float wayPointChangeDistance = .5f;


    private NavMeshAgent _agent;
    private GameObject _player;

    // Start is called before the first frame update
    void Start()
    {
        _agent = GetComponent<NavMeshAgent>();
        _agent.SetDestination(wayPoints[currentWayPointIdx].position);

        
    }

    // Update is called once per frame
    void Update()
    {
        if(currentState == EnemyState.patrol)
        {
        
            if(!_agent.pathPending && _agent.remainingDistance < wayPointChangeDistance)
            {
                ChangeWayPoint();
            }
        }
        else if (currentState == EnemyState.chase)
        {
            _agent.SetDestination(_player.transform.position);
        }
    }

    //Enemy cycles through different waypoints
    private void ChangeWayPoint()
    {
        if(currentWayPointIdx < wayPoints.Length -1)
        {
            currentWayPointIdx++;
        }
        else
        {
            currentWayPointIdx = 0;   
        }

        _agent.SetDestination(wayPoints[currentWayPointIdx].position);
    }

    //make it so when player gets close enough, enemy chases them
    private void OnTriggerEnter(Collider other)
    {
        if(other.gameObject.tag == "Player")
        {
            currentState = EnemyState.chase;
            _player = other.gameObject;
        }
    }
    
    //make it so when player gets far away enough, enemy stops chasing them
    private void OnTriggerExit(Collider other)
    {
        if(other.gameObject.tag == "Player")
        {
            currentState = EnemyState.patrol;
            _player = null;
            _agent.SetDestination(wayPoints[currentWayPointIdx].position);
        }
    }
}
