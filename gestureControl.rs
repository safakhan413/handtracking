
// // set up packages
// cargo init
// cargo add tungstenite url serde_json // and maybe more packages
// // to run it
// cargo run

// Steven Zahanov's code copied and modified that can be used with Safa's


// https://doc.rust-lang.org/book/ch12-02-reading-a-file.html
// https://stackoverflow.com/questions/69933869/how-can-i-make-a-rust-websocket-client

use std::fs;
// https://blog.devgenius.io/getting-started-with-websockets-and-json-data-in-rust-84434ddbfc21
use tungstenite::{connect, Message};
use url::Url;
use serde_json;
use std::time::Duration;
use std::thread::sleep;

fn main() {

    // Connect to a websocket server
    let (mut socket, _response) = connect(Url::parse("ws://remotescontrol1.herokuapp.com/5fa89a529623b645aa04690b").unwrap()).expect("Can't connect");

    sleep(Duration::from_millis(1000));
    // https://stackoverflow.com/questions/28952938/how-can-i-put-the-current-thread-to-sleep

    loop {

        let contents = fs::read_to_string("F:\\coding exercises\\handtracking\\direction.txt")
            .expect("error here");

        if (contents == "up") {
            println!("{}", contents);

            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 4, \"command\": \"HIGH\" }".into())).unwrap();
            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 14, \"command\": \"HIGH\" }".into())).unwrap();
        }

        if (contents == "down") {
            println!("{}", contents);

            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 12, \"command\": \"HIGH\" }".into())).unwrap();
            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 15, \"command\": \"HIGH\" }".into())).unwrap();
        }

        if (contents == "left") {
            println!("{}", contents);

            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 4, \"command\": \"HIGH\" }".into())).unwrap();
            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 15, \"command\": \"HIGH\" }".into())).unwrap();
        }

        if (contents == "right") {
            println!("{}", contents);

            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 12, \"command\": \"HIGH\" }".into())).unwrap();
            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 14, \"command\": \"HIGH\" }".into())).unwrap();
        }

        if (contents == "none") {
            println!("{}", contents);

            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 4, \"command\": \"LOW\" }".into())).unwrap();
            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 12, \"command\": \"LOW\" }".into())).unwrap();
            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 14, \"command\": \"LOW\" }".into())).unwrap();
            socket.write_message(Message::Text("{ \"type\": \"GPIO\", \"pin\": 15, \"command\": \"LOW\" }".into())).unwrap();
        }

        sleep(Duration::from_millis(100)); // slow down to every 0.1 seconds

    }

}



/*
// these package/cargo verions seemed to work
tungstenite = "0.16.0"
serde_json = "1.0.78"
url = "2.2.2"
time = "0.3.36"
*/


