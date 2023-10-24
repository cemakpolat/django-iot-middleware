import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { DeviceComponent } from './components/device/device.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatInputModule } from '@angular/material/input'; // Import other modules as needed
import { MatCardModule } from '@angular/material/card';

@NgModule({
  declarations: [
    AppComponent,
    DeviceComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatCardModule, 
    MatInputModule, 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
