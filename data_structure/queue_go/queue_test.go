package queue_go

import "testing"

func TestQueue(t *testing.T) {
	queue := NewQueue(5)
	for i := 1; i <= 5; i++ {
		if queue.Enqueue(i) != true {
			t.Fatalf("Enqueue Error")
		}
	}
	t.Logf("Queue current length is %d", queue.Length())
	if queue.Length() != 5 {
		t.Fatalf("Queue Length Error")
	}
	if queue.Enqueue(6) != false {
		t.Fatalf("This operation should return false, because queue is full")
	}
	queue.Dequeue()
	t.Logf("queue.head: %d, queue.tail %d", queue.head, queue.tail)
	queue.Dequeue()
	t.Logf("queue.head: %d, queue.tail %d", queue.head, queue.tail)
	if queue.Length() != 3 {
		t.Fatalf("Queue Length Error")
	}
	if queue.Enqueue(6) == false {
		t.Fatalf("Enqueue Error")
	}
	t.Logf("queue.head: %d, queue.tail %d", queue.head, queue.tail)
	if queue.Length() != 4 {
		t.Fatalf("Queue Length Error")
	}
	queue.Dequeue()
	queue.Dequeue()
	queue.Dequeue()
	queue.Dequeue()
	t.Logf("queue.head: %d, queue.tail %d", queue.head, queue.tail)
	exceptionDequeue := func() {
		defer func() {
			if err := recover(); err == nil {
				t.Fatalf("This occur error here")
			} else {
				if e, ok := err.(EmptyQueueException); ok != true {
					t.Fatalf("This occur error here")
				} else {
					t.Logf(e.Error())
				}
			}
		}()
		queue.Dequeue()
	}
	exceptionDequeue()
	queue.Enqueue(7)
	t.Logf("queue.head: %d, queue.tail %d", queue.head, queue.tail)
	queue.Enqueue(8)
	t.Logf("queue.head: %d, queue.tail %d", queue.head, queue.tail)
}
