import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListComponent } from './list/list.component';
import { RouterModule, Routes } from '@angular/router';
import { ApiService } from '../api.service';
import { MatListModule } from '@angular/material/list';

const routes: Routes = [
  {
    path: '',
    component: ListComponent,
  },
  {
    path: 'device/:deviceId',
    component: ListComponent,
  },
];

@NgModule({
  declarations: [
    ListComponent
  ],
  imports: [
    CommonModule,
    MatListModule,
    RouterModule.forChild(routes),
  ],
  providers: [
    ApiService,
  ],
})
export class MessageModule { }
