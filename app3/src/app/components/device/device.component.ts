import { Component, OnInit } from '@angular/core';
import { WebSocketService } from '../../websocket.service';

@Component({
  selector: 'app-device',
  templateUrl: './device.component.html',
  styleUrls: ['./device.component.css']
})
export class DeviceComponent implements OnInit {
  deviceData: any;

  constructor(private webSocketService: WebSocketService) {}

  ngOnInit(): void {
    this.webSocketService.getMessageDevice().subscribe({
      next:  msg => {
        console.log('message received: ' + JSON.stringify(msg) ) ;
        this.deviceData=JSON.stringify(msg);}, // Called whenever there is a message from the server.
      error: err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
      complete: () => console.log('complete') // Called when connection is closed (for whatever reason).
     });
  }
}

