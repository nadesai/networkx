#!/usr/bin/env python
from nose.tools import *
from networkx import *
from networkx.generators.product import *

class TestGeneratorsProduct():
    def smoke_test_product_graph(self):
        seed = 42
        G=kronecker_random_graph(5,[[0.1,0.1],[0.1,0.1]],seed)
        G=fast_kronecker_random_graph(5,[[0.1,0.1],[0.1,0.1]],seed)

    def test_kronecker(self):
        m=[[0,0],[0,0]]
        G=kronecker_random_graph(4,m,directed=False)
        assert_equal(len(G),2**4)
        assert_equal(len(G.edges()),0)

        m=[[1,1],[1,1]]
        G=kronecker_random_graph(4,m)
        assert_equal(len(G),2**4)
        assert_equal(len(G.edges()),(2**4)**2)

        m=[[1,1],[1,1]]
        G=kronecker_random_graph(4,m,directed=False)
        assert_equal(len(G),16)
        assert_equal(len(G.edges()),136)

        m=[[1,0],[0,0]]
        G=kronecker_random_graph(4,m)
        assert_equal(len(G.edges()),1)
        assert_true(G.has_edge(0,0))
        assert_true(not G.has_edge(0,1))

        m=[[1,1],[0,0]]
        G=kronecker_random_graph(4,m)
        assert_equal(len(G.edges()),16)
        for i in range(16):
            assert_true(G.has_edge(0,i))

        m=[[1,1],[1,0]]
        G=kronecker_random_graph(4,m,directed=False)
        assert_equal(len(G),16)
        assert_equal(len(G.edges()),41)

        m=[[1,1],[0,0]]
        G=kronecker_random_graph(0,m)
        assert_equal(len(G),1)
        assert_equal(len(G.edges()),0)

        m=[[1,1]]
        assert_raises(networkx.exception.NetworkXError,
                kronecker_random_graph,4,m)

        m=[[1,1],[0,1]]
        assert_raises(networkx.exception.NetworkXError,
                kronecker_random_graph,4,m,None,False)

        m=[[2,1],[1,1]]
        assert_raises(networkx.exception.NetworkXError,
                kronecker_random_graph,4,m)


    def test_fast_kronecker(self):
        m=[[0,0],[0,0]]
        G=fast_kronecker_random_graph(4,m,directed=False)
        assert_equal(len(G),2**4)
        assert_equal(len(G.edges()),0)

        m=[[1,1],[1,1]]
        G=fast_kronecker_random_graph(4,m)
        assert_equal(len(G),16)
        assert_equal(len(G.edges()),256)

        m=[[1,1],[1,1]]
        G=fast_kronecker_random_graph(4,m,directed=False)
        assert_equal(len(G),16)
        assert_equal(len(G.edges()),136)

        m=[[1,0],[0,0]]
        G=fast_kronecker_random_graph(4,m)
        assert_equal(len(G.edges()),1)
        assert_true(G.has_edge(0,0))
        assert_true(not G.has_edge(0,1))

        m=[[1,1],[0,0]]
        G=fast_kronecker_random_graph(4,m)
        assert_equal(len(G.edges()),16)
        for i in range(16):
            assert_true(G.has_edge(0,i))

        m=[[1,1],[0,0]]
        G=fast_kronecker_random_graph(0,m)
        assert_equal(len(G),1)
        assert_equal(len(G.edges()),0)

        m=[[1,1],[1,0]]
        G=fast_kronecker_random_graph(4,m,directed=False)
        assert_equal(len(G),16)
        assert_equal(len(G.edges()),41)

        m=[[1,1]]
        assert_raises(networkx.exception.NetworkXError,
                fast_kronecker_random_graph,4,m)

        m=[[1,1],[0,1]]
        assert_raises(networkx.exception.NetworkXError,
                fast_kronecker_random_graph,4,m,None,False)

        m=[[2,1],[1,1]]
        assert_raises(networkx.exception.NetworkXError,
                fast_kronecker_random_graph,4,m)

