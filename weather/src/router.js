import Vue from 'vue'
import Router from 'vue-router'
import Frame from "@/components/Frame";
import WgGraph from "@/components/WgGraph";
import RxGraph from "@/components/RxGraph";

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            children: [
                {
                    path: 'wgGraph',
                    component: WgGraph
                }, {
                    path: 'rxGraph',
                    component: RxGraph
                }
            ],
            component: Frame,
            redirect: 'wgGraph'
        }
    ]
})
