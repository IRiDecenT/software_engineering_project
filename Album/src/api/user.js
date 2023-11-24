import request from '@/utils/request'


export const userRegister = (registerData) => {
    return request({
        method: 'POST',
        url: '/register/',
        headers: {
            'Content-Type': 'application/json'
        },
        data: registerData
    })
}

export const userLogin = (loginData) => {
    return request({
        method: 'POST',
        url: '/login/',
        headers: {
            'Content-Type': 'application/json'
        },
        data: loginData
    })
}