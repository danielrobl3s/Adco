PGDMP     #                     {            adco    15.1    15.1 
               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16400    adco    DATABASE     f   CREATE DATABASE adco WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE adco;
                postgres    false            �            1259    16406 	   proyectos    TABLE       CREATE TABLE public.proyectos (
    id_proyecto integer NOT NULL,
    proyecto character varying(30),
    institucion character varying(20),
    fecha_inicio date,
    fecha_termino date,
    telefono integer,
    direccion character varying(50),
    ubicacion character varying(50)
);
    DROP TABLE public.proyectos;
       public         heap    postgres    false            �            1259    16411    trabajadores_proveedores    TABLE     �  CREATE TABLE public.trabajadores_proveedores (
    id integer NOT NULL,
    nombre character varying(50),
    telefono integer,
    correo character varying(50),
    direccion character varying(50),
    especialidad character varying(20),
    concepto character varying(20),
    archivos character varying(100),
    contratos character varying(50),
    monto_contrato double precision,
    abonos double precision,
    saldo double precision
);
 ,   DROP TABLE public.trabajadores_proveedores;
       public         heap    postgres    false                      0    16406 	   proyectos 
   TABLE DATA           �   COPY public.proyectos (id_proyecto, proyecto, institucion, fecha_inicio, fecha_termino, telefono, direccion, ubicacion) FROM stdin;
    public          postgres    false    214   �                 0    16411    trabajadores_proveedores 
   TABLE DATA           �   COPY public.trabajadores_proveedores (id, nombre, telefono, correo, direccion, especialidad, concepto, archivos, contratos, monto_contrato, abonos, saldo) FROM stdin;
    public          postgres    false    215   �       s           2606    16410    proyectos proyectos_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.proyectos
    ADD CONSTRAINT proyectos_pkey PRIMARY KEY (id_proyecto);
 B   ALTER TABLE ONLY public.proyectos DROP CONSTRAINT proyectos_pkey;
       public            postgres    false    214            u           2606    16415 6   trabajadores_proveedores trabajadores_proveedores_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.trabajadores_proveedores
    ADD CONSTRAINT trabajadores_proveedores_pkey PRIMARY KEY (id);
 `   ALTER TABLE ONLY public.trabajadores_proveedores DROP CONSTRAINT trabajadores_proveedores_pkey;
       public            postgres    false    215                  x������ � �            x������ � �     