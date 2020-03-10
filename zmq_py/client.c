#include <zmq.h>
#include <czmq.h>
#include <stdio.h>

// gcc -Wall -g client.c -std=c99 -lzmq -lczmq -o client

int main(void) {

	printf ("Connecting to python server...\n");
    zsock_t *socket = zsock_new_req("tcp://localhost:5555");

    zmsg_t *msg = zmsg_new ();
	assert (msg);

	char* function = "exp(t)*y(t)";
    char* function_name = "y";
    char* function_variable = "t";
    float initial_x = 0.0;
    float initial_f = 1.0;
    float constant = 1.0;

	// add string to the message
	zmsg_addstrf(msg, "%s", function);
	zmsg_addstrf(msg, "%s", function_name);
	zmsg_addstrf(msg, "%s", function_variable);
	zmsg_addstrf(msg, "%f", initial_x);
	zmsg_addstrf(msg, "%f", initial_f);
	zmsg_addstrf(msg, "%f", constant);

    // send message
	int rc = zmsg_send (&msg, socket);
	assert (rc == 0);
	assert (!msg);

	//receive response
    msg = zmsg_recv(socket);
    assert(msg);

    char* answer = zmsg_popstr(msg);
    printf("%s\n ", answer);

    zmsg_destroy(&msg);
    zsock_destroy(&socket);
	return 0;
}