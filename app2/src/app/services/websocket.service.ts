import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class WebSocketService {
  private socket: WebSocketSubject<any>;
  
  constructor() {
    // Access environment variables
    const wsBaseUrl = environment.wsBaseUrl;
    const deviceId = environment.deviceId;
    
    // Replace the URL with your WebSocket server URL
    this.socket = webSocket(wsBaseUrl+'/ws/device/'+deviceId+'/') 
  }
  getMessageDevice(){
    return this.socket.asObservable();
  }
  sendMessage(message: any): void {
    this.socket.next(message);
  }
}
